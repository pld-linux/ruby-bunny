%define gem_name bunny
Summary:	Synchronous Ruby AMQP 0.9.1 client
Name:		ruby-%{gem_name}
Version:	0.7.9
Release:	2
License:	MIT
Group:		Development/Languages
URL:		http://github.com/ruby-amqp/bunny
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	9984619cb0bd727485c3bf26a00af336
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	setup.rb
Requires:	ruby
# Disabled for now; tests disabled due to need for running rabbitmq server
#BuildRequires: rubygem(rspec)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A synchronous Ruby AMQP client that enables interaction with
AMQP-compliant brokers.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q
cp -p %{_datadir}/setup.rb .

%build
%{__ruby} setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

%{__ruby} setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
%{__ruby} setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.textile CHANGELOG
%{ruby_libdir}/bunny.rb
%{ruby_libdir}/bunny
%{ruby_libdir}/qrack

%if 0
%files doc
%defattr(644,root,root,755)
%endif
