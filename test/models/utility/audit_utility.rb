require_relative 'elasticsearch_utility.rb'

module AuditUtility

  def self.get_all_audits
    ElasticsearchUtility.refresh "reveal~system~001"
    ElasticsearchUtility.get_audits['hits']['hits']
  end

end
