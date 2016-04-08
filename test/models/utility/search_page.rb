require_relative '../utility/emcui_utility.rb'
require_relative '../utility/searchui_utility.rb'
require_relative 'paging_helper.rb'
require_relative 'sort_helper.rb'

class SearchPage < BrowserContainer
  include EmcUiUtility
  include PagingHelper
  include SortHelper
  include SearchUiUtility
  
  SUB_URI = "search"
  URL = "#{URL}/#{SUB_URI}"

  # wait for page loading
  def loaded?
    # Watir::Wait.until { emc_loading('loading').present? }
    sleep 3
    emc_loading('loading').wait_while_present
  end
  
  
  # wait for search results loaded
  def results_loaded?
    # Watir::Wait.until { emc_loading('loading').present? }
    sleep 2
    emc_loading('loading').wait_while_present    

  end
  
  def logged_in? user
    emc_profile_menu_label.text.include? user
  end
  
  def logout
    emc_profile_menu_label.click
    @browser.div(:class =>/emc-profile-menu-item/, :text => "Logout" ).wait_until_present
    @browser.div(:class => /emc-profile-menu-item/, :text => "Logout").click 
    next_page = SearchLoginPage.new(@browser)
    next_page
  end
  
  def show_filters
    @browser.span( :text =>"Add | Remove Filters").click unless @browser.div( :class =>"filter-panel" ).present?
  end
  
  def hide_filters
    @browser.span( :text =>"Add | Remove Filters").click if @browser.div( :class =>"filter-panel" ).present?
  end
  
  def refresh
    @browser.refresh
    loaded?
  end
  

  #get filter : applications
  def applications
      emc_combo_menu_dropdown_button('applicationList').click
      item_list = emc_combo_menu_items('applicationList')
      appList=[]
      item_list.each { |item|
         appList.push item.text  
      }
      emc_combo_menu_dropdown_button('applicationList').click
      
      return appList
  end
  
  #set filter : applications
  def applications= appList
    emc_input_checkbox("Application").set
    # @browser.div( :id => "applicationList" ).span( :class => "emc-combo-menu-arrow emc-arrow-down").click
    if appList != nil
      # Expand the drop down list
      emc_combo_menu_dropdown_button('applicationList').click
      item_list = emc_combo_menu_items('applicationList')
      # Get not used index list
      item_list.each do |item|
          if appList.include? (item.text)
            item.checkbox.set
          else
            item.checkbox.set(false)
          end
      end
      # Collapse the dropdown list
      emc_combo_menu_dropdown_button('applicationList').click
    end
  end
  
  #get filter items: indexes
  def indexes
      emc_combo_menu_dropdown_button('indexList').click
      item_list = emc_combo_menu_items('indexList')
      idxList=[]
      item_list.each { |item|
         idxList.push item.text  
      }
      emc_combo_menu_dropdown_button('indexList').click
      
      return idxList
  end
  
  #set filter: indexes
  def indexes= idxList
    emc_input_checkbox("Index").set
    # @browser.div( :id => "applicationList" ).span( :class => "emc-combo-menu-arrow emc-arrow-down").click
    if idxList != nil
      # Expand the drop down list
      emc_combo_menu_dropdown_button('indexList').click
      item_list = emc_combo_menu_items('indexList')
      # Get not used index list
      item_list.each do |item|
          if idxList.include? (item.text)
            item.checkbox.set
          else
            item.checkbox.set(false)
          end
      end
      # Collapse the dropdown list
      emc_combo_menu_dropdown_button('indexList').click
    end
  end
  
  def search_types
      emc_combo_menu_dropdown_button('indexList').click
      item_list = emc_combo_menu_items('indexList')
      idxList=[]
      item_list.each { |item|
         idxList.push item.text  
      }
      emc_combo_menu_dropdown_button('indexList').click
      
      return idxList
  end
  
  def search_types= typeList
    emc_input_checkbox("Search Types").set
    if typeList != nil
      # Expand the drop down list
      emc_combo_menu_dropdown_button('searchTypeList').click
      item_list = emc_combo_menu_items('searchTypeList')
      # Get not used index list
      item_list.each do |item|
          if typeList.include? (item.text)
            item.checkbox.set
          else
            item.checkbox.set(false)
          end
      end
      # Collapse the dropdown list
      emc_combo_menu_dropdown_button('searchTypeList').click
    end
  end
  
  def keyword= keyword
    emc_search_textbox.set(keyword)
  end
  
  def search 
    emc_search_button.click
    results_loaded?
  end
  
  def summary
    if @browser.span( :id => "revealSummary" ).present?
       return @browser.span( :id => "revealSummary" ).text 
    elsif @browser.span( :class => /label-text, error-message/ ).present?
       return @browser.span( :class => /label-text, error-message/ ).text 
    else 
    end 
  end

  ########################
  # For aggregation start
  ########################
  def click_file_type_chart
    @browser.text_field(:id => 'input-filetype').parent.parent.button.click
  end
  
  def click_piechart_icon piechart_id
    #@browser.text_field(:id => piechart_id).parent.parent.button.click
    @browser.button(:id => piechart_id).click
  end
  
  def highcharts_customized_data_model
    sleep(5)
    highchart_paths = nil
    highchart_data_labels = nil
    @browser.div(:id => 'highcharts-2').svg.elements.each do |element|
      if element.outer_html.include?('highcharts-series highcharts-tracker')
        highchart_paths = element.paths
      elsif element.outer_html.include?('highcharts-data-labels highcharts-tracker')
        highchart_data_labels = element.gs.map {|g| g.text}
      end
    end
    return highchart_data_labels, highchart_paths
  end
  
  def search_results_count 
     @browser.span( :id => "revealSummary" ).text.match(/Found (\d+) results/).captures.first.to_i
  end   
  
  def search_results_titles is_cross_app = false
     results = Array.new
	 @browser.divs( :class => "emc-data-list-item" ).each do |item|
	    one_result = Hash.new
	    one_result['title'] = item.link(  :class => "emc-item-title").text
	    item.span(  :text => "Index:").parent.spans.each do |span|
	      if span.text != "Index:"
	        one_result['index'] = span.text
	      end
	    end
	    if is_cross_app
        item.span(  :text => "Application:").parent.spans.each do |span|
          if span.text != "Application:"
            one_result['app'] = span.text
          end
        end
	    end
	    results << one_result
	 end
	 return results
  end    

  def click_chart item_name
    highchart_data_labels, highchart_paths = highcharts_customized_data_model
    highchart_data_labels.zip(highchart_paths).each do |label, path|
      path.click if label == item_name
    end
    sleep(5) #work around temporary
  end
  ########################
  # For aggregation end
  ########################
  
  #get the action button list for item
  def itemactions itemindex = 0, text = ''
    item = nil
    actionlist = Array.new()
    if (text == '')
      item = emc_data_list_item(itemindex)
    else
      item = emc_data_list_item_by_text(text)
    end    
    item.element(:tag_name => 'action').buttons.each do |button|
      p button.text
      actionlist.push(button.text)
    end
    return actionlist
  end  
  
  def click_item_detail_action_button itemindex = 0, text = ''
    item = nil
    if (text == '')
      item = emc_data_list_item(itemindex)
    else
      item = emc_data_list_item_by_text(text)
    end    
    item.span(:text => 'Detail').click
  end
  
  def close_detail_window redirect
    if(redirect == false)
      @browser.div(:class => /emc-message-frame/).wait_until_present
      sleep 1
      @browser.button(:id => 'ok').click
      return true
    else
      @browser.window(:title => /^Action Service/).wait_until_present
      sleep 1        
      return true
    end    
    return false
  end  
  
  def user_preference
    emc_profile_menu_label.click
    @browser.div(:class =>/emc-profile-menu-item/).wait_until_present
    @browser.div(:class => /emc-profile-menu-item/, :index => 1).click 
    
    # wait for the user preference frame
    emc_combo_menu_dropdown_button('idLocaleItems').wait_until_present
  end
  
  def get_locale_list
      emc_combo_menu_dropdown_button('idLocaleItems').click
      localeList = []
      @browser.div(:id=>'idLocaleItems').elements(:tag_name => 'li', :class=> 'emc-combo-menu-item').each do |item|
        localeList.push item.span.text
      end
      @browser.div(:id=>'idLocaleItems').element(:tag_name => 'li', :class=> 'emc-combo-menu-item  emc-current-item').click
      return localeList
  end
  
  def get_current_locale
      emc_combo_menu_dropdown_button('idLocaleItems').click
      curlocale = @browser.div(:id=>'idLocaleItems').element(:tag_name => 'li', :class=> 'emc-combo-menu-item  emc-current-item')
      localetext = curlocale.span.text
      curlocale.click
      return localetext
  end
  
  def set_locale locale
    emc_combo_menu_dropdown_button('idLocaleItems').click
    @browser.div(:id=>'idLocaleItems').elements(:tag_name => 'li', :class=> 'emc-combo-menu-item').each do |item|
      if item.span.text==locale
        item.click
        break
      end
    end
  end
  
  def get_restore_maxhit
    return @browser.text_field(:id => 'maxHit').value 
  end
  
  def set_restore_maxhit value
    return @browser.text_field(:id => 'maxHit').set(value)
  end
  
  def wait_preference_error_tip message
    @browser.div(:class=>/alert alert-danger preference_error_tip ng-binding/, :text => message).wait_until_present
  end
  
  def save_user_preference
    @browser.button(:id => 'save').click
    sleep 3
    loaded?
  end
  
  def close_user_preference
    return @browser.div(:class => 'emc-message-close ng-scope').click
  end
  
  def click_help
    emc_profile_menu_label.click
    @browser.div(:class =>/emc-profile-menu-item/, :text => "Help" ).wait_until_present
    @browser.div(:class => /emc-profile-menu-item/, :text => "Help").click 
    # get the help page
  end

  def click_about
    emc_profile_menu_label.click
    @browser.div(:class =>/emc-profile-menu-item/, :text => "About" ).wait_until_present
    @browser.div(:class => /emc-profile-menu-item/, :text => "About").click 
    @browser.input(:value => "Reveal Web").wait_until_present
    #wait for the about frame
  end  
  

  def click_item_action_button action, itemindex = 0, text = ''
    item = nil
    if (text == '')
      item = emc_data_list_item(itemindex)
    else
      item = emc_data_list_item_by_text(text)
    end    
    item.span(:text => action).click
  end

  def get_preview_item_content redirect
    if(redirect == false)
      @browser.div(:class => /emc-message-frame/).wait_until_present
    else
      @browser.window(:title => /^Action Service/).wait_until_present
    end 
    return @browser.div(:class => /emc-message-body-inner ng-scope/).text
  end

  def get_versions hash
    click_about
    titles_hash = hash.clone
    titles_hash.each do |key, value|
      titles_hash[key] = get_version_by_title(key)
    end
    titles_hash
  end  
  
  def get_version_by_title title
    version = nil
    @browser.divs(:class => 'emc-form-row').each do |div|
      if div.input(:value => title).exists?
        version = div.div(:class => 'emc-form-row-input').input.value
      end
    end
    return version   
  end

end
