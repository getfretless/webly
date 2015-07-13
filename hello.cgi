#!/usr/bin/env ruby
require 'cgi'
require 'erb'

cgi = CGI.new
page = 'home'
page = cgi['page'] unless cgi['page'].empty?

puts cgi.header

greetings = ['Mr. President', 'Your Royal Majesty', 'Your Highness']
if cgi['name'].empty?
  greeting = greetings.sample
else
  greeting = cgi['name']
end

def layout(page_name, &block)
  title = { 'home'  => 'Welcome', 'about' => 'About Us' }
  template = File.read 'layout.html.erb'
  puts ERB.new(template).result(binding)
end

def render_view(view_name)
  template = File.read("#{view_name}.html.erb")
  ERB.new(template).result(binding)
end

layout page do
  if page.downcase == 'about'
    render_view page
  else
    render_view 'index'
  end
end
