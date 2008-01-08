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
Version:	1.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e45f32723485de6af929c7fd3bc55743
Patch0:		%{name}-nointeractivebuild.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(POE) >= 0.38
BuildRequires:	perl(LWP::ConnCache)
BuildRequires:	perl(LWP::UserAgent)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module makes serving up HTTP requests a breeze in POE.

The hardest thing to understand in this module is the HANDLERS. That's it!

The standard way to use this module is to do this:


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
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/Server/*.pm
%{perl_vendorlib}/POE/Component/Server/SimpleHTTP
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
