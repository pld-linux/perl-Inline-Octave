%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pname	Octave
Summary:	Inline::Octave perl module
Summary(pl):	Modu³ perla Inline::Octave
Name:		perl-Inline-Octave
Version:	0.16
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.4
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	octave
Requires:	octave
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Octave - Inline octave code into your perl.

%description -l pl
Modu³ Inline::Octave - pozwalaj±cy na umieszczanie kodu w jêzyku
Octave w skryptach perlowych.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
echo '/usr/bin/octave' | perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Inline/Octave.pm
%{_mandir}/man3/*
