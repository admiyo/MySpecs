# Generated from rjb-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname rjb
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Ruby Java bridge
Name: rubygem-%{gemname}
Version: 1.2.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rjb.rubyforge.org/
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires:  java >= 1.5
BuildRequires: rubygems
BuildRequires: ruby-devel
BuildRequires: java-devel  


Provides: rubygem(%{gemname}) = %{version}

%description
RJB is a bridge program that connect between Ruby and Java with Java Native
Interface.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
JAVA_HOME=/usr/lib/jvm/java gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}



pushd %{buildroot}%{gemdir}/gems/%{gemname}-%{version}/ext
make clean
sed -e 's!RUBYLIBDIR = .*!RUBYLIBDIR = $(sitearchdir)$(target_prefix)!' \
    -e 's!RUBYARCHDIR = .*!RUBYARCHDIR = $(sitearchdir)$(target_prefix)!' \
    < Makefile > Makefile.new
mv Makefile.new Makefile
make clean
popd

/usr/lib/rpm/find-debuginfo.sh
#for now just delete it.  Eventually, we want a debuginfo rpm
rm -f %{buildroot}/usr/lib/debug/usr/lib/ruby/gems/1.8/gems/rjb-%{version}/lib/rjbcore.so.debug

rm -rd  %{buildroot}/usr/lib/debug



%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 31 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 1.2.0-1
- Initial package
