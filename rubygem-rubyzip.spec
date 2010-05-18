# Generated from rubyzip-0.9.1.gem by gem2rpm -*- rpm-spec -*-
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname rubyzip
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A ruby module for reading and writing zip files
Name: rubygem-%{gemname}
Version: 0.9.4
Release: 3%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubyzip.sourceforge.net/
Source0: Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(abi) = 1.8
Requires: rubygems
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
rubyzip is a ruby module for reading and writing zip files


%package doc
Summary: Documentation for %{name}
Group: Documentation

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

chmod 755 %{buildroot}%{geminstdir}/install.rb

for SCRIPT in example_filesystem gtkRubyzip example write_simple qtzip zipfind
do
	chmod 755  %{buildroot}%{geminstdir}/samples/$SCRIPT.rb
done

for RB in stdrubyext zip tempfile_bugfixed ioextras zipfilesystem ziprequire
do
	chmod 644  %{buildroot}%{geminstdir}/lib/zip/$RB.rb
done

chmod 644  %{buildroot}%{geminstdir}/Rakefile

# These aren't executables
sed -i -e '/^#!\/usr\/bin\/env ruby/d' \
  %{buildroot}%{geminstdir}/Rakefile 

# CRLF is sprinkled throughout the files
#find %{buildroot}%{geminstdir} -type f -print0 | xargs -0 -n1 sed -i 's/\r//'
sed -i 's/\r//'  %{buildroot}%{geminstdir}/samples/write_simple.rb



%check
pushd %{buildroot}%{gemdir}/gems/%{gemname}-%{version}/
rake test
popd


%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/[A-Z]*
%dir %{geminstdir}
%{geminstdir}/install.rb
%{geminstdir}/lib
%{geminstdir}/samples
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-,root,root,-)
%{geminstdir}/Rakefile
%{geminstdir}/test
%{gemdir}/doc/%{gemname}-%{version}


%changelog
* Thu May 13 2010 Adam Young <ayoung@redhat.com> - 0.9.4-2
- Upgraded to 0.9.4, with a patch to make buildr run


* Tue May 11 2010 Adam Young <ayoung@redhat.com> - 0.9.1-2
- Split documentation out into separate rpm
- Fixed rpmlint errors

* Tue May 11 2010 Adam Young <ayoung@redhat.com> - 0.9.1-2
- Fixed License
- Added ABI Dependency
- changed define to global

* Tue Apr 06 2010 Adam Young <ayoung@redhat.com> - 0.9.1-1
- Initial package
