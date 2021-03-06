# Generated from net-ssh-2.0.21.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname net-ssh
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Net::SSH: a pure-Ruby implementation of the SSH2 client protocol
Name: rubygem-%{gemname}
Version: 2.0.21
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/net-ssh/net-ssh
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(abi) = 1.8 
Requires: rubygems
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.


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
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/THANKS.rdoc
%doc %{geminstdir}/CHANGELOG.rdoc
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 31 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 2.0.21-1
- Initial package
