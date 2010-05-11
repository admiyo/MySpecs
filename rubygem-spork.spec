# Generated from spork-0.8.2.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname spork
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: spork
Name: rubygem-%{gemname}
Version: 0.8.2
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/timcharper/spork
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(abi) = 1.8
Requires: rubygems
BuildRequires: rubygems
Provides: rubygem(%{gemname}) = %{version}

%description
A forking Drb spec server


%prep
%setup -q -c -T

%build
gem install --local --install-dir .%{gemdir}\
            --force --rdoc %{SOURCE0}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
cp -R  . %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x


mkdir -p %{buildroot}/usr/share/doc/%{gemdir}-%{version}
for DOC in MIT-LICENSE README.rdoc 
    do mv  %{buildroot}%{geminstdir}/$DOC %{buildroot}/usr/share/doc/%{gemdir}-%{version} 
done	


%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/spork
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc /usr/share/doc/%{gemdir}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Tue May 11 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 0.8.2-2
- Changed define to global
- Removed duplication of files
- Corrected License
- Added Ruby ABI dependency

* Wed Mar 31 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 0.8.2-1
- Initial package
