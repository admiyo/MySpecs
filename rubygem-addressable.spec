# Generated from addressable-2.1.1.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname addressable
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: URI Implementation
Name: rubygem-%{gemname}
Version: 2.1.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://addressable.rubyforge.org/
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(abi) = 1.8
Requires: rubygems
Requires: rubygem(rake) >= 0.7.3
Requires: rubygem(rspec) >= 1.0.8
Requires: rubygem(launchy) >= 0.3.2
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Addressable is a replacement for the URI implementation that is part of
Ruby's standard library. It more closely conforms to the relevant RFCs and
adds support for IRIs and URI templates.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}



mkdir -p %{buildroot}/usr/share/doc/%{gemdir}-%{version}
mv  %{buildroot}%{geminstdir}/README %{buildroot}/usr/share/doc/%{gemdir}-%{version}


%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc /usr/share/doc/%{gemdir}-%{version}


%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Thu Apr 01 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 2.1.1-1
- Initial package
