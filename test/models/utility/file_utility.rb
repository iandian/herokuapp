#encoding: utf-8
require 'net/ssh'
module FileUtility
  def delete_file file_list, host = '', username = '', password = ''
    if host == '' && username == '' && password ==''
      delete_local_file(file_list)
    else
      delete remote_file(file_list, host, username, password)
    end
  end
  
  def file_exists? file_list, host = '', username = '', password = ''
    if host == '' && username == '' && password ==''
      local_file_exists?(file_list)
    else
      remote_file_exists?(file_list, host, username, password)
    end
  end
   
  def remote_file_exists? file_list, host, username, password
    result = true
    if get_remote_client_os(host, username, password) == "Windows"
      file_list.length.times do |i|
        file_list[i] = "/cygdrive/#{file_list[i]}"  
      end     
    end
    Net::SSH.start(host, username, :password => password) do |ssh|
      file_list.length.times do |i|
        cmd = "ls \"#{file_list[i]}\""
        result = (ssh.exec!(cmd).rstrip.force_encoding('UTF-8') == file_list[i])
        break if result == false    
      end
    end
    result
  end
  
  def delete_remote_file file_list, host, username, password
    if get_remote_client_os(host, username, password) == "Windows"
      file_list.length.times do |i|
        file_list[i] = "cygdrive/#{file_list[i]}"  
      end     
    end
    Net::SSH.start(host, username, :password => password) do |ssh|
      file_list.length.times do |i|
        cmd = "rm \"#{file_list[i]}\""
        puts ssh.exec!(cmd)      
      end
    end
  end
  
  def get_remote_client_os host, username, password
    os = ""
    cmd = "uname -a"
    Net::SSH.start(host, username, :password => password) do |ssh|
      result = ssh.exec!(cmd)
      puts result
      if result.include? "Linux"
        os = "Linux"
      elsif result.include? "WIN_NT"
        os = "Windows"
      end
    end
    os
  end
  
  def local_file_exists? file_list
    result = true
    file_list.each do |file|
      result = File::exists?(file)
      break if result == false
    end
    return result
  end
  
  def delete_local_file file_list
    file_list.each do |file|
      if File::exists?(file)
        File.delete(file)
      end
    end
  end
  
  def remove_folder folder_path
    cmd = "sudo rm -r \"#{folder_path}\""
    puts `#{cmd}`
  end
end