#!/usr/bin/ruby
require 'json'
require 'hashie'
require 'pathname'
require_relative '../utility/controller_type.rb'

class Index

  attr_accessor :name
  attr_accessor :types

  def initialize(name, file_path)
    @name = name
    @parser = Parser.new(file_path)
	@types = parser.types
  end



end
