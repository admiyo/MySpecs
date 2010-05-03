# Generated from libxml-ruby-1.1.3.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname libxml-ruby
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Ruby libxml bindings
Name: rubygem-libxml
Version: 1.1.4
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://libxml.rubyforge.org/
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
BuildRequires: rubygems
Provides: rubygem(%{gemname}) = %{version}

%description
The Libxml-Ruby project provides Ruby language bindings for the GNOME Libxml2
XML toolkit. It is free software, released under the MIT License.
Libxml-ruby's primary advantage over REXML is performance - if speed  is your
need, these are good libraries to consider, as demonstrated by the informal
benchmark below.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon May 3 2010 Adam Young  <ayoung@ayoung.boston.devel.redhat.com> - 1.1.3-2
- Changed RPM name to conform to Fedora standards
- Ugraded to libxml-ruby 1.1.4

* Sat Apr 17 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 1.1.3-1
- Initial package
