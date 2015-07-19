#!/usr/bin/env ruby
require 'cgi'
require 'erb'
require_relative 'webly'

cgi = CGI.new
puts cgi.header

webly = Webly.new
webly.layout(cgi['page']) do
  if cgi['page'] != ''
    webly.render_view(cgi['page'])
  else
    webly.render_view('index')
  end
end
