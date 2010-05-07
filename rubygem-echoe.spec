# Generated from echoe-4.3.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname echoe
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A Rubygems packaging tool that provides Rake tasks for documentation, extension compiling, testing, and deployment
Name: rubygem-%{gemname}
Version: 4.3
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://blog.evanweaver.com/files/doc/fauna/echoe/
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(abi) = 1.8
Requires: rubygems
Requires: rubygem(gemcutter) >= 0
Requires: rubygem(rubyforge) >= 0
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A Rubygems packaging tool that provides Rake tasks for documentation,
extension compiling, testing, and deployment.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

mkdir -p %{buildroot}/usr/share/doc/%{gemdir}-%{version}
for DOC in LICENSE CHANGELOG README TODO
    do mv  %{buildroot}%{geminstdir}/$DOC %{buildroot}/usr/share/doc/%{gemdir}-%{version} 
done	


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
* Wed Mar 31 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 4.3-1
- Initial package
