# Generated from echoe-4.3.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname echoe
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A Rubygems packaging tool that provides Rake tasks for documentation, extension compiling, testing, and deployment
Name: rubygem-%{gemname}
Version: 4.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://blog.evanweaver.com/files/doc/fauna/echoe/
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
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

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README
%doc %{geminstdir}/TODO
%doc %{geminstdir}/lib/echoe.rb
%doc %{geminstdir}/lib/echoe/extensions.rb
%doc %{geminstdir}/lib/echoe/platform.rb
%doc %{geminstdir}/lib/echoe/rubygems.rb
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 31 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 4.3-1
- Initial package
