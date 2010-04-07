# Generated from rubyzip-0.9.1.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname rubyzip
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: rubyzip is a ruby module for reading and writing zip files
Name: rubygem-%{gemname}
Version: 0.9.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubyzip.sourceforge.net/
Source0: %{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
rubyzip is a ruby module for reading and writing zip files


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
* Tue Apr 06 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 0.9.1-1
- Initial package
