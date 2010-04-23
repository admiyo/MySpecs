# Generated from linecache-0.43.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname linecache
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Read file with caching
Name: rubygem-%{gemname}
Version: 0.43
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubyforge.org/projects/rocky-hacks/linecache
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
BuildRequires: rubygems
Provides: rubygem(%{gemname}) = %{version}

%description
LineCache is a module for reading and caching lines. This may be useful for
example in a debugger where the same lines are shown many times.


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
%doc %{geminstdir}/README
%doc %{geminstdir}/lib/linecache.rb
%doc %{geminstdir}/lib/tracelines.rb
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Fri Apr 23 2010 Adam Young <ayoung@redhat.com> - 0.43-1
- Initial package
