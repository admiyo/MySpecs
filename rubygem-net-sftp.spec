# Generated from net-sftp-2.0.4.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname net-sftp
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A pure Ruby implementation of the SFTP client protocol
Name: rubygem-%{gemname}
Version: 2.0.4
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://net-ssh.rubyforge.org/sftp
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(net-ssh) >= 2.0.9
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A pure Ruby implementation of the SFTP client protocol


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
%doc %{geminstdir}/CHANGELOG.rdoc
%doc %{geminstdir}/lib/net/sftp/constants.rb
%doc %{geminstdir}/lib/net/sftp/errors.rb
%doc %{geminstdir}/lib/net/sftp/operations/dir.rb
%doc %{geminstdir}/lib/net/sftp/operations/download.rb
%doc %{geminstdir}/lib/net/sftp/operations/file.rb
%doc %{geminstdir}/lib/net/sftp/operations/file_factory.rb
%doc %{geminstdir}/lib/net/sftp/operations/upload.rb
%doc %{geminstdir}/lib/net/sftp/packet.rb
%doc %{geminstdir}/lib/net/sftp/protocol/01/attributes.rb
%doc %{geminstdir}/lib/net/sftp/protocol/01/base.rb
%doc %{geminstdir}/lib/net/sftp/protocol/01/name.rb
%doc %{geminstdir}/lib/net/sftp/protocol/02/base.rb
%doc %{geminstdir}/lib/net/sftp/protocol/03/base.rb
%doc %{geminstdir}/lib/net/sftp/protocol/04/attributes.rb
%doc %{geminstdir}/lib/net/sftp/protocol/04/base.rb
%doc %{geminstdir}/lib/net/sftp/protocol/04/name.rb
%doc %{geminstdir}/lib/net/sftp/protocol/05/base.rb
%doc %{geminstdir}/lib/net/sftp/protocol/06/attributes.rb
%doc %{geminstdir}/lib/net/sftp/protocol/06/base.rb
%doc %{geminstdir}/lib/net/sftp/protocol/base.rb
%doc %{geminstdir}/lib/net/sftp/protocol.rb
%doc %{geminstdir}/lib/net/sftp/request.rb
%doc %{geminstdir}/lib/net/sftp/response.rb
%doc %{geminstdir}/lib/net/sftp/session.rb
%doc %{geminstdir}/lib/net/sftp/version.rb
%doc %{geminstdir}/lib/net/sftp.rb
%doc %{geminstdir}/README.rdoc
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 31 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 2.0.4-1
- Initial package
