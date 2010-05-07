# Generated from webmock-0.9.1.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname webmock
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Library for stubbing HTTP requests in Ruby
Name: rubygem-%{gemname}
Version: 0.9.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+
URL: http://github.com/bblimke/webmock
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(abi) = 1.8
Requires: rubygems
Requires: rubygem(addressable) >= 2.1.1
Requires: rubygem(rspec) >= 1.2.9
Requires: rubygem(httpclient) >= 2.1.5.2
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
WebMock allows stubbing HTTP requests and setting expectations on HTTP
requests.


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
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.md
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 31 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 0.9.1-1
- Initial package
