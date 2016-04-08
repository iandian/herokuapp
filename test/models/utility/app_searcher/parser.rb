#!/usr/bin/ruby
require 'json'
require 'set'
require 'hashie'
require 'pathname'
require_relative '../utility/controller_type.rb'

class Parser

  attr_reader :types

  def initialize(file_path)
    @file_path = file_path
    @json = parse_file_to_json(@file_path)
    pn = Pathname.new(file_path)
	@types = Set.new
  end


  def search type, field, value
    
#    field = field.to_sym
    result = Array.new
    	  case type
		when ControllerType::String, ControllerType::Query_string   then
		 result = result | @json.select {|h1| h1.key?(field) and !h1[field].nil? and h1[field].include? value}
		when ControllerType::Multiple_string   then
		   (value.split(",").map(&:strip)).each{|v| 
                      result = result | @json.select {|h1| h1.key?(field) and !h1[field].nil? and h1[field].downcase.include? v.downcase}}
		when ControllerType::Date   then
		  result =  result | @json.select {|h1| h1.key?(field) and !h1[field].nil? and (h1[field]<=> value['gte']) > -1 && (h1[field]<=> value['lte']) < 1}
    when ControllerType::Numeric   then
                  result = result | @json.select {|h1| h1.key?(field) and !h1[field].nil? and (h1[field] >= value['min'].to_i) and (h1[field] <= value['max'].to_i) }
		when ControllerType::Boolean   then
                  result = result | @json.select {|h1| h1.key?(field) and !h1[field].nil? and  h1[field].downcase == value.to_s.downcase}	   
	  end
	  return result
  end

  def method_missing(name, *args)
    name = name.to_s
    is_fit = (name =~ /^search_/)? true : false
    is_type = false
    type = (name.sub! 'search_', '')
    ControllerType.constants.each do |c|
     ( ControllerType.const_get(c).include? type)  ? (is_type = true) : next
    end
    is_type = true if type == 'batch'
    super unless is_fit and is_type
    result = Array.new
    field = nil
    value = nil
    if type == 'batch'
      count = 0
      args[0][:batch].each do |a|
        search_type = a[:type]
        a.each do |key, v|
          if key.to_s != 'type'
            field = key.to_s
            value = v 
          end
        end
      if count == 0
         result = send('search', search_type, field, value)
      else
         result = result & send('search', search_type, field, value)
      end
      count = count + 1
      end
      
    else
      args[0].each do |key, v|
        field = key.to_s
        value = v
      end        
    result = result | send('search', type, field, value)
    end
    result.each do |item|
      item['_app'] = @app
      item['_index'] = @index
    end
    return result
  end

  def parse_file_to_json file_path
    text = File.read(file_path, mode: 'r:bom|utf-8')
    text.gsub!(/\r\n?/, "\n")
    content = '['
	type = ''
    text.each_line do |line|
      if line =~ /index/i && line =~ /_type/i || line.strip.empty?
	    unless line.strip.empty?
		  type = JSON.parse(line)['index']['_type']
		  @types.add type
		end
        next
      end
      content << (line.gsub("\}\n", ", \"_type\": \"#{type}\"\},\n"))
    end
    return JSON.parse(content.chop.chop << ']')
  end
  
  def fix_cp1252_utf8(text)
    text.encode('cp1252',
                :fallback => {
                  "\u0081" => "\x81".force_encoding("cp1252"),
                  "\u008D" => "\x8D".force_encoding("cp1252"),
                  "\u008F" => "\x8F".force_encoding("cp1252"),
                  "\u0090" => "\x90".force_encoding("cp1252"),
                  "\u009D" => "\x9D".force_encoding("cp1252")
                })
        .force_encoding("utf-8")
  end

end
