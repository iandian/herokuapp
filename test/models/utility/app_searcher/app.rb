#!/usr/bin/ruby
require 'json'
require 'pathname'

class App

  attr_reader :indexes
  attr_reader :types

  def initialize(file_path)
    @file_path = file_path
	@types = Array.new	
	@indexes = Array.new	
	parse_indexes
	parse_types
	parse_local
	parse_presentations
  end

  def parse_indexes
    indexes = 
  end

  def parse_types
    item = Hash.new
	find_file_and_parse_to_json(/^types.json/)['types'].map {|j| item['type'] = j}
	find_files_and_parse_to_jsons(/^searchcols-/).map {|j| j['search_cols']}
  end
  
  def parse_local
    
  end
  
  def parse_presentations
    
  end 
  
  def find_file_and_parse_to_json pattern
  parse_to_json(@file_path.children.detect {|path|  path.basename.to_s =~ pattern})
  end
  
  def find_files_and_parse_to_jsons pattern
  @file_path.children.select {|path|  path.basename.to_s =~ pattern}.map {|i| parse_to_json i }
  end
  
  def parse_to_json pathname
    JSON.parse(pathname.read(mode: 'r:bom|utf-8'))
  end
  
end
