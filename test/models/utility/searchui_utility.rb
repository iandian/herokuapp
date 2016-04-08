require 'time'
require_relative '../utility/emcui_utility.rb'
require_relative '../utility/parser.rb'
require_relative '../utility/multi_parser.rb'
require_relative '../utility/controller_type.rb'

module SearchUiUtility


  def get_div_contains_controller title
    @browser.divs(:class => 'emc-form-row').each do |div|
      return div if div.span(:text => title).exists?
    end
	  #parent = @browser.span(:text => title)
	  #parent = parent.parent until parent.tag_name == 'div' and parent.class_name == 'emc-form-row'	  
	end

	def get_controller_values title, controller_type
	  parent = get_div_contains_controller(title)
	  values = Array.new
	  case controller_type
		when ControllerType::String   then
		   values.push(parent.select_list.text)
		when ControllerType::Query_string   then
		   values.push(parent.text_field.text)
		when ControllerType::Multiple_string   then
		   values.push(parent.text_field.text)
		when ControllerType::Date   then
		   values.push(parent.text_field(:placeholder => "Start: yyyy-MM-dd").text)
		   values.push(parent.text_field(:placeholder => "End: yyyy-MM-dd").text)
		when ControllerType::Boolean   then
		   values.push(parent.select_list.text)
		when ControllerType::Numeric   then
		   values.push(parent.text_field(:placeholder => "Min:").text)
		   values.push(parent.text_field(:placeholder => "Max:").text)	   
	  end
	  return values
	end


	def set_controller_values title, controller_type, values
	  emc_input_checkbox(title).set
	  parent = get_div_contains_controller(title)
	  controller = parent
	  case controller_type
		when ControllerType::String   then
		   parent.select_list.select_value(values)
		when ControllerType::Query_string   then
		   parent.text_field.set(values)
		when ControllerType::Multiple_string   then
		   parent.text_field.set(values)
		when ControllerType::Date   then
		   parent.text_field(:placeholder => "Start: yyyy-MM-dd").set(convert_to_localtime(values["gte"]))
		   parent.text_field(:placeholder => "End: yyyy-MM-dd").set(convert_to_localtime(values["lte"]))
		when ControllerType::Boolean   then
       parent.select.select(values=='true' ? 'Yes':'No') 
		when ControllerType::Numeric   then
		   parent.text_field(:placeholder => "Min:").set(values["min"])
		   parent.text_field(:placeholder => "Max:").set(values["max"])  
	  end
	end

  def convert_to_localtime value
    Time.parse(value).localtime.strftime("%Y-%m-%d")
  end

end
