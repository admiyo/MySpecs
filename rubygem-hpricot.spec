# Generated from hpricot-0.8.2.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname hpricot
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: a swift, liberal HTML parser with a fantastic library
Name: rubygem-%{gemname}
Version: 0.8.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://code.whytheluckystiff.net/hpricot/
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
BuildRequires: rubygems
Provides: rubygem(%{gemname}) = %{version}

%description
a swift, liberal HTML parser with a fantastic library


%prep
%setup -q -c -T

%build

gem install --local --install-dir .%{gemdir} --force --rdoc %{SOURCE0}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
cp -R  . %{buildroot}


mkdir -p %{buildroot}/usr/share/doc/%{gemdir}-%{version}
for DOC in COPYING CHANGELOG README
do 
   mv  %{buildroot}%{geminstdir}/$DOC \
       %{buildroot}/usr/share/doc/%{gemdir}-%{version} 
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
* Fri Apr 09 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 0.8.2-1
- Initial package
