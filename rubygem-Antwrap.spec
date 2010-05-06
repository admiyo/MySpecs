# Generated from Antwrap-0.7.0.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname Antwrap
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A Ruby module that wraps the Apache Ant build tool. Antwrap can be used to invoke Ant Tasks from a Ruby or a JRuby script
Name: rubygem-%{gemname}
Version: 0.7.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubyforge.org/projects/antwrap/
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(rjb) >= 1.0.3
Requires: rubygem(hoe) >= 1.3.0
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A Ruby module that wraps the Apache Ant build tool. Antwrap can be used to
invoke Ant Tasks from a Ruby or a JRuby script.  == FEATURES/PROBLEMS: 
Antwrap runs on the native Ruby interpreter via the RJB (Ruby Java Bridge gem)
and on the JRuby interpreter. Antwrap is compatible with Ant versions 1.5.4, 
1.6.5 and 1.7.0. For more information, 	see the Project Info
(http://rubyforge.org/projects/antwrap/) page.   == SYNOPSIS:  Antwrap is a
Ruby library that can be used to invoke Ant tasks. It is being used in the
Buildr (http://incubator.apache.org/buildr/) project to execute  Ant
(http://ant.apache.org/) tasks in a Java project. If you are tired of fighting
with Ant or Maven XML files in your Java project, take some time to  check out
Buildr!


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
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.txt
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 31 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 0.7.0-1
- Initial package
