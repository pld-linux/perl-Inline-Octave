#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pname	Octave
Summary:	Inline::Octave - inline octave code into your perl
Summary(pl):	Inline::Octave - umieszczanie kodu octave w kodzie perlowym
Name:		perl-Inline-Octave
Version:	0.20
Release:	1	
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
# Source0-md5:	4c590abe9d4073cc35a3ad8a6322c763
BuildRequires:	perl-devel >= 5.8
BuildRequires:	perl-Inline >= 0.4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	octave
Requires:	octave
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Octave Perl module gives you the power of the octave
programming language from within your Perl programs.

%description -l pl
Modu³ Perla Inline::Octave umo¿liwia korzystanie z mocy jêzyka
programowania octave wewn±trz skryptów w Perlu.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
echo '/usr/bin/octave' | perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Inline/Octave.pm
%{_mandir}/man3/*
