#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-Server-SimpleHTTP
Summary:	POE::Component::Server::SimpleHTTP - Perl extension to serve HTTP requests in POE.
#Summary(pl):	
Name:		perl-POE-Component-Server-SimpleHTTP
Version:	1.36
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7668387ad3020f0c43c163860665d6be
Patch0:		%{name}-nointeractivebuild.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(IPC::Shareable)
BuildRequires:	perl(POE::Component::Client::HTTP)
BuildRequires:	perl(POE::Component::SSLify) 
BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(POE) >= 0.38
# wyglada na to ze jednak perl(POE) > 0.9999 bo z 0.9989 nie fafa (wali duzo testow)
BuildRequires:	perl(LWP::ConnCache)
BuildRequires:	perl(LWP::UserAgent)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module makes serving up HTTP requests a breeze in POE.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/Server/*.pm
%{perl_vendorlib}/POE/Component/Server/SimpleHTTP
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
