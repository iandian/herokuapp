# config valid only for current version of Capistrano
lock '3.4.0'

set :application, 'herokuapp', default_run_options[:pty] = true
set :repo_url, 'emc@10.98.20.20:~/git/herokuapp/.git'
set :deploy_to, "/var/www/#{fetch(:application)}" 
set :linked_files, %w{config/database.yml}
set :default_env, { rvm_bin_path: '~/.rvm/bin' }
set(:config_files, %w(
  nginx.conf
))

set(:symlinks, [
  {
    source: "nginx.conf",
    link: "/opt/nginx/conf/nginx.conf"
  }
 ]
)
# Default branch is :master
# ask :branch, `git rev-parse --abbrev-ref HEAD`.chomp

# Default deploy_to directory is /var/www/my_app_name
# set :deploy_to, '/var/www/my_app_name'

# Default value for :scm is :git
# set :scm, :git

# Default value for :format is :pretty
# set :format, :pretty

# Default value for :log_level is :debug
# set :log_level, :debug

# Default value for :pty is false
# set :pty, true

# Default value for :linked_files is []
# set :linked_files, fetch(:linked_files, []).push('config/database.yml', 'config/secrets.yml')

# Default value for linked_dirs is []
# set :linked_dirs, fetch(:linked_dirs, []).push('log', 'tmp/pids', 'tmp/cache', 'tmp/sockets', 'vendor/bundle', 'public/system')

# Default value for default_env is {}
# set :default_env, { path: "/opt/ruby/bin:$PATH" }

# Default value for keep_releases is 5
# set :keep_releases, 5

namespace :deploy do

 after 'deploy:finished', 'deploy:setup_config'
 before 'deploy:setup_config', 'nginx:remove_default_conf'

  # reload nginx to it will pick up any modified vhosts from
  # setup_config
  after 'deploy:setup_config', 'nginx:reload'


end
