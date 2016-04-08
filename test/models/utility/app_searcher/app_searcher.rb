#!/usr/bin/ruby
require 'json'
require 'hashie'
require 'pathname'
require_relative '../utility/controller_type.rb'

class AppSearcher

  def initialize(app_folder_path)
    pn = Pathname.new(app_folder_path)
    @app = pn.basename.to_s
    presentation_app_global = JSON.parse(pn.children.detect {|path|  path.basename.to_s == "presentation-app_global.json"}.read(mode: 'r:bom|utf-8'))
	locale = JSON.parse(pn.children.detect {|path|  path.basename.to_s == "locale-en_us.json"}.read(mode: 'r:bom|utf-8'))
	search_types = JSON.parse(pn.children.detect {|path|  path.basename.to_s == "locale-en_us.json"}.read(mode: 'r:bom|utf-8'))
	indexes = pn.children.select {|path|  path.basename.to_s =~ /^search_/}.map {|i| JSON.parse(i.read(mode: 'r:bom|utf-8')) }
	bulks = pn.children.select {|path|  path.basename.to_s =~ /^search_/}.map {|i| JSON.parse(i.read(mode: 'r:bom|utf-8')) }
	searchcols = pn.children.select {|path|  path.basename.to_s =~ /^search_/}.map {|i| JSON.parse(i.read(mode: 'r:bom|utf-8')) }
	
  end


  def search filters, sort = nil
    results = search_results(filters)
	return sort.nil? results : sort_results(results, sort)  
  end
  
  def search_results filters
    titles = Hash.new
    filters.map{ |key, value| }    # 取出local中的对应数据
	                               # 从presentation_app_global取出controller_type, field,
								   # 取出search_type
								   # 对每个index， 拼出search的filter， search对应search_type的result
								   # 从result中，按照presentation_type.json的要求，去除不需要的数据
								   # 合并返回result
  end

end
