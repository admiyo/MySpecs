# Generated from fakefs-0.2.1.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname fakefs
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A fake filesystem. Use it in your tests
Name: rubygem-%{gemname}
Version: 0.2.1
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/defunkt/fakefs
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = 1.8
Requires: rubygems
BuildRequires: rubygems
BuildRequires: rubygem(rake)
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A fake filesystem. Use it in your tests.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/usr/share/doc/%{gemdir}-%{version}
for DOC in README.markdown LICENSE
    do mv  %{buildroot}%{geminstdir}/$DOC %{buildroot}/usr/share/doc/%{gemdir}-%{version} 
done	

%check
pushd %{buildroot}%{gemdir}/gems/%{gemname}-%{version}/
#rake test
rake spec
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{geminstdir}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%doc /usr/share/doc/%{gemdir}-%{version}

%changelog
* Tue May 11 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 0.2.1-2
- Updated License
- Converted define to global
- Added dependencies to get a clean build inside of mock
- Added call to tests in the check stage
- Removed duplicate files entries

* Wed Mar 31 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 0.2.1-1
- Initial package
