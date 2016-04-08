$TestFileName=__FILE__
require "watir-webdriver"
require_relative "../../common/testcase.rb"
require_relative "../common/common.rb"
require_relative "../page/search_login_page.rb"
require_relative "../page/search_page.rb"


class TestSearchFilter < Reveal::TestCase

  def setup
    @site = Site.new(Watir::Browser.new BrowserContainer.get_browser_type)
  end
  
   def check_filter_with_oneapp testcase
    testcase[:parameter_list].zip(testcase[:validation_list]).each do |p, v|  
      account = p['account']
      password = p['password']
        
      search_login_page = @site.search_login_page.open
      search_page = search_login_page.login(account, password)
      search_page.applications = p['application']
	    search_page.set_controller_values(p['title'], p['controller_type'], p['values'])
      search_page.search
      search_page.page_size=100
	    actual_results_titles = search_page.search_results_titles false
	    actual_results_count = search_page.search_results_count
	    pa = Parser.new(File.realpath(__FILE__)+p['data_file_path'])
	    expect_results = pa.send "search_#{p['controller_type']}", {p['field'].to_sym => p['values']}
	    assert(actual_results_count == expect_results.count, "Expected search result count: #{expect_results.count}, actual search result count: #{actual_results_count}") 
      expect_results.each do |result|
        assert(!!(actual_results_titles.detect {|h1| h1['title'] == result['name'][/.*(?=\..+$)/]}) , "Expected search result with title: #{result['name']} not list in search result") 
      end	  
    end
  end
  
   def check_multiple_filters_with_oneapp testcase
    testcase[:parameter_list].zip(testcase[:validation_list]).each do |p, v|  
      account = p['account']
      password = p['password']
        
      search_login_page = @site.search_login_page.open
      search_page = search_login_page.login(account, password)
      search_page.applications = p['application']
	    query = Hash.new
	    array = Array.new
	    p['feilds_list'].each do |f|
	       m = f['feilds']
         search_page.set_controller_values(m['title'], m['controller_type'], m['values'])
		     array << { :type => m['controller_type'], m['field'].to_sym => m['values'] }
      end	  
      query[:batch] = array
      search_page.search
      search_page.page_size=100
	    actual_results_titles = search_page.search_results_titles false
	    actual_results_count = search_page.search_results_count
	    pa = Parser.new(File.realpath(__FILE__)+p['data_file_path'])
	    expect_results = pa.send "search_batch", query
	    assert(actual_results_count == expect_results.count, "Expected search result count: #{expect_results.count}, actual search result count: #{actual_results_count}") 
      expect_results.each do |result|
        assert(!!(actual_results_titles.detect {|h1| h1['title'] == result['name'][/.*(?=\..+$)/]}) , "Expected search result with title: #{result['name']} not list in search result") 
      end	  
    end
  end 
  
   def check_filter_cross_app testcase
    testcase[:parameter_list].zip(testcase[:validation_list]).each do |p, v|  
      account = p['account']
      password = p['password']
        
      search_login_page = @site.search_login_page.open
      search_page = search_login_page.login(account, password)
      search_page.applications = p['application']
      search_page.set_controller_values(p['title'], p['controller_type'], p['values'])
      search_page.search
      search_page.page_size=100
      actual_results_array = search_page.search_results_titles true
      actual_results_count = search_page.search_results_count
      pa = MultiParser.new(p['data_file_path'].map{ |a| File.realpath(__FILE__)+a })
      expect_results = pa.send "search_#{p['controller_type']}", {p['field'].to_sym => p['values']}
      assert(actual_results_count == expect_results.count, "Expected search result count: #{expect_results.count}, actual search result count: #{actual_results_count}") 
      actual_results_array.each do |result|
        title_field = p['result_titles'][result['app']] 
        assert(!!expect_results.detect {|h1| h1.key?(title_field) and !h1[title_field].nil?  and h1[title_field] == result['title'] and h1['_app'] == result['app'] and h1['_index'] == result['index']}, 
                  "Search result : #{result} with title filed #{p['result_titles'][result['app']] } should not list in search result") 
      end   
    end
  end
  
  def teardown
    @site.capture_screenshot(@method_name) if not passed?
    @site.close
  end
end
