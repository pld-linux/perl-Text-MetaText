#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	MetaText
Summary:	Text::MetaText Perl module
Summary(cs):	Modul Text::MetaText pro Perl
Summary(da):	Perlmodul Text::MetaText
Summary(de):	Text::MetaText Perl Modul
Summary(es):	M�dulo de Perl Text::MetaText
Summary(fr):	Module Perl Text::MetaText
Summary(it):	Modulo di Perl Text::MetaText
Summary(ja):	Text::MetaText Perl �⥸�塼��
Summary(ko):	Text::MetaText �� ����
Summary(nb):	Perlmodul Text::MetaText
Summary(pl):	Modu� Perla Text::MetaText
Summary(pt):	M�dulo de Perl Text::MetaText
Summary(pt_BR):	M�dulo Perl Text::MetaText
Summary(ru):	������ ��� Perl Text::MetaText
Summary(sv):	Text::MetaText Perlmodul
Summary(uk):	������ ��� Perl Text::MetaText
Summary(zh_CN):	Text::MetaText Perl ģ��
Name:		perl-Text-MetaText
Version:	0.22
Release:	11
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4a2b5d120459dcb678cac876c99fa805
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-File-Recurse
BuildRequires:	perl-TimeDate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::MetaText Perl module.

%description -l cs
Modul Text::MetaText pro Perl.

%description -l da
Perlmodul Text::MetaText.

%description -l de
Text::MetaText Perl Modul.

%description -l es
M�dulo de Perl Text::MetaText.

%description -l fr
Module Perl Text::MetaText.

%description -l it
Modulo di Perl Text::MetaText.

%description -l ja
Text::MetaText Perl �⥸�塼��

%description -l ko
Text::MetaText �� ����.

%description -l nb
Perlmodul Text::MetaText.

%description -l pl
Modu� Perla Text::MetaText.

%description -l pt
M�dulo de Perl Text::MetaText.

%description -l pt_BR
M�dulo Perl Text::MetaText.

%description -l ru
������ ��� Perl Text::MetaText.

%description -l sv
Text::MetaText Perlmodul.

%description -l uk
������ ��� Perl Text::MetaText.

%description -l zh_CN
Text::MetaText Perl ģ��

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
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
%doc Changes README Todo Features
%attr(755,root,root) %{_bindir}/metapage
%{perl_vendorlib}/Text/MetaText.pm
%{perl_vendorlib}/Text/MetaText
%{_mandir}/man[13]/*
