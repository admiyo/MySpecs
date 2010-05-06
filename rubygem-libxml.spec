# Generated from libxml-ruby-1.1.3.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname libxml-ruby
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Ruby libxml bindings
Name: rubygem-%{gemname}
Version: 1.1.4
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://libxml.rubyforge.org/
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
BuildRequires: rubygems
BuildRequires: ruby-devel
BuildRequires: zlib-devel
BuildRequires: libxml2
BuildRequires: libxml2-devel

Provides: rubygem(%{gemname}) = %{version}

%description
The Libxml-Ruby project provides Ruby language bindings for the GNOME Libxml2
XML toolkit. It is free software, released under the MIT License.
Libxml-ruby's primary advantage over REXML is performance - if speed  is your
need, these are good libraries to consider, as demonstrated by the informal
benchmark below.


%prep
%setup -cT

%build
mkdir -p %{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force --rdoc %{SOURCE0}

rm $( find . -name libxml-ruby.so.a )


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
cp -R  . %{buildroot}


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
- Ugraded to libxml-ruby 1.1.4

* Sat Apr 17 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 1.1.3-1
- Initial package
