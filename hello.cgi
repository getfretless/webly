#!/usr/bin/env ruby
require 'cgi'
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
  puts "<!doctype html><html><head><title>#{title[page_name]}</title></head><body>"
  puts yield
  puts '</body></html>'
end

def render_view(view_name)
  puts File.read("#{view_name}.html")
end

layout page do
  if page.downcase == 'about'
    render_view page
  else
    render_view 'index'
  end
end
