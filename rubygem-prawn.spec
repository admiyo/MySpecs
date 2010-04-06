# Generated from prawn-0.8.4.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname prawn
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A fast and nimble PDF generator for Ruby
Name: rubygem-%{gemname}
Version: 0.8.4
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://wiki.github.com/sandal/prawn
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(prawn-core) >= 0.8.4
Requires: rubygem(prawn-core) < 0.9
Requires: rubygem(prawn-layout) >= 0.8.4
Requires: rubygem(prawn-layout) < 0.9
Requires: rubygem(prawn-security) >= 0.8.4
Requires: rubygem(prawn-security) < 0.9
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Prawn is a fast, tiny, and nimble PDF generator for Ruby


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
* Wed Mar 31 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 0.8.4-1
- Initial package
