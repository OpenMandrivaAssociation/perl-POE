%define	upstream_name	 POE
%define upstream_version 1.286

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
Epoch:		2

Summary:	Portable multitasking and networking framework for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz
# This upstream_name naming scheme does not follow path names...

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:  perl(Curses)
Buildrequires:  perl(IO::Pty)
Buildrequires:  perl(IO::Tty)
Buildrequires:  perl(POE::Test::Loops)
Buildrequires:  perl(Socket6)
Buildrequires:  perl(Term::ReadKey)
Buildrequires:  perl-libwww-perl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Provides:	perl(POE::Resource::Controls)

%description
POE is a framework for cooperative, event driven multitasking in Perl.

POE originally was developed as the core of a persistent object server and
runtime environment. It has evolved into a general purpose multitasking and
networking framework, encompassing and providing a consistent interface to
other event loops such as Event and the Tk and Gtk toolkits.

POE is a mature framework for creating multitasking programs in Perl.  It has
been in active development since 1998.  It has been used in mission-critical
systems such as internetworked financial markets, file systems, commerce and
application servers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 755 examples
chmod 755 examples/*.perl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --default
%make

%check
DISPLAY= %{__make} test

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES HISTORY README examples TODO
%{perl_vendorlib}/POE
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
