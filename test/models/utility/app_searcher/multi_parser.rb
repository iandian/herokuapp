#!/usr/bin/ruby
require_relative '../utility/controller_type.rb'
require_relative '../utility/parser.rb'

class MultiParser

  def initialize(files_path_array)
    @parser_hash = Hash.new
    files_path_array.each do |file_path|
      parser = Parser.new(file_path)
      @parser_hash[file_path] = parser
    end
  end


  def method_missing(name, *args)
    method_name = name.to_s
    is_fit = (method_name =~ /^search_/)? true : false
    is_type = false
    type = (method_name.sub! 'search_', '')
    ControllerType.constants.each do |c|
     ( ControllerType.const_get(c).include? type)  ? (is_type = true) : next
    end
    is_type = true if type == 'batch'
    super unless is_fit and is_type
    result = Array.new
    @parser_hash.each do |key, v|
      result.concat(v.send name, args[0])
    end
    return result
  end

end
