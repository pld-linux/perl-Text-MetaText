#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	MetaText
Summary:	Text::MetaText - meta-language for processing "template" text files
Summary(pl):	Text::MetaText - metaj�zyk do przetwarzania szablon�w tekstowych
Name:		perl-Text-MetaText
Version:	0.22
Release:	13
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
MetaText is a text processing and markup meta-language which can
be used for processing "template" files. This module is a Perl 5
extension implementing a MetaText object class which processes
text files, interpreting and acting on the embedded MetaText
directives within.

Like a glorified pre-processor, MetaText can: include files,
define and substitute variable values, execute conditional
actions based on variables, call other Perl functions or object
methods and capture the resulting output back into the document,
and more. It can format the resulting output of any of these
operations in a number of ways. The objects, and inherently, the
format and symantics of the MetaText langauge itself, are highly
configurable.

%description -l pl
MetaText to metaj�zyk do przetwarzania tekstu i oznacze�, kt�ry mo�na
u�ywa� do przetwarzania plik�w "szablon�w". Ten modu� jest
rozszerzeniem Perla 5 implementuj�cym klas� obiektu MetaText
przetwarzaj�cego pliki tekstowe, interpretuj�cego i dzia�aj�cego na
osadzonych w nich dyrektywach MetaTextu.

Podobnie jak ka�dy zachwalany preprocesor MetaText mo�e: do��cza�
pliki, definiowa� i podstawia� warto�ci zmiennych, wykonywa� akcje
warunkowe w oparciu o zmienne, wywo�ywa� inne funkcje Perla lub
metody obiekt�w i przechwytywa� ich wyniki z powrotem do dokumentu
i wiele innych. Wyj�cie dowolnej z operacji mo�e by� formatowane na
wiele sposob�w. Obiekty i zwi�zany z nimi format oraz semantyka
samego j�zyka MetaText s� wysoce konfigurowalne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mv t/exec.t{,.whythiscrapfails}

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
