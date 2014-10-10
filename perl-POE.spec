%define	upstream_name	 POE
%define upstream_version 1.311

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
Epoch:		2

Summary:	Portable multitasking and networking framework for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz
# This upstream_name naming scheme does not follow path names...

BuildRequires:	perl-devel
BuildRequires:	perl(Curses)
BuildRequires:	perl(IO::Pty)
BuildRequires:	perl(IO::Tty)
BuildRequires:	perl(POE::Test::Loops)
BuildRequires:	perl(Socket6)
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl-libwww-perl
BuildArch:	noarch
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
perl Makefile.PL INSTALLDIRS=vendor --default
%make

%check
DISPLAY= make test

%install
%makeinstall_std

%files
%doc CHANGES HISTORY README examples TODO
%{perl_vendorlib}/POE
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*


%changelog
* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.311.0-1mdv2011.0
+ Revision: 682142
- update to new version 1.311

* Fri Apr 29 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.310.0-1
+ Revision: 660584
- new version

* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.294.0-1mdv2011.0
+ Revision: 602387
- update to new version 1.294

* Mon Sep 06 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.293.0-1mdv2011.0
+ Revision: 576302
- update to 1.293

* Sun Aug 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.292.0-1mdv2011.0
+ Revision: 569954
- update to 1.292

* Tue Jul 27 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.291.0-1mdv2011.0
+ Revision: 561629
- update to 1.291

* Tue Apr 06 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.289.0-1mdv2011.0
+ Revision: 532160
- update to 1.289

* Tue Feb 23 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.287.0-1mdv2010.1
+ Revision: 510096
- update to 1.287

* Mon Feb 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.286.0-1mdv2010.1
+ Revision: 506247
- update to 1.286

* Thu Jan 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.284.0-1mdv2010.1
+ Revision: 491459
- update to 1.284

* Fri Jan 08 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.283.0-1mdv2010.1
+ Revision: 487513
- update to 1.283

* Thu Jan 07 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.282.0-1mdv2010.1
+ Revision: 487052
- update to 1.282

* Sun Jan 03 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.281.0-1mdv2010.1
+ Revision: 485807
- update to 1.281

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.280.0-1mdv2010.1
+ Revision: 461254
- adding missing buildrequires:
- update to 1.280

* Thu Sep 24 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.269.0-1mdv2010.0
+ Revision: 448126
- update to 1.269

* Thu Sep 17 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.268.0-1mdv2010.0
+ Revision: 443881
- update to 1.268

* Wed Sep 09 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.267.0-1mdv2010.0
+ Revision: 435713
- update to 1.267

* Sun Aug 30 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.266.0-1mdv2010.0
+ Revision: 422563
- update to 1.266

* Sat Aug 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.20.0-1mdv2010.0
+ Revision: 422084
- update to 1.020

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.7.0-2mdv2010.0
+ Revision: 408651
- force rebuild
- update to 1.007

* Mon Jun 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.6.0-1mdv2010.0
+ Revision: 381789
- update to 1.006
- using %%perl_convert_version
- fixed license field

* Fri May 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.005-1mdv2010.0
+ Revision: 369670
- update to new version 1.005

* Wed Oct 29 2008 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.003-1mdv2009.1
+ Revision: 298547
- updated to 1.003

* Fri Jun 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.0003-1mdv2009.0
+ Revision: 229483
- update to new version 1.0003

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.0002-1mdv2009.0
+ Revision: 208372
- update to new version 1.0002
- update to new version 1.0002

* Mon Apr 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.0001-1mdv2009.0
+ Revision: 196164
- update to new version 1.0001

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.0000-1mdv2009.0
+ Revision: 193918
- update to new version 1.0000

* Tue Jan 22 2008 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:0.9999-2mdv2008.1
+ Revision: 156501
- force 5.10.0 rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.9999-1mdv2008.0
+ Revision: 55830
- update to new version 0.9999

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 2:0.9989-1mdv2008.0
+ Revision: 20447
- 0.9989


* Wed Feb 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9917-1mdv2007.0
+ Revision: 127180
- new version

* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 2:0.3601-2mdv2007.1
+ Revision: 73470
- import perl-POE-0.3601-2mdv2007.1

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.3601-1mdv2007.0
- New version 0.3601

* Thu Jun 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 20.3502-1mdv2007.0
- New version 0.3502

* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.3501-1mdv2007.0
- New release 0.3501

* Sun Apr 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.3401-1mdk
- New release
- spec cleanup

* Thu Feb 02 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2:0.3301-1mdk
- 0.3301

* Sat Sep 24 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2:0.3202-1mdk
- new version
- rpmbuildupdate aware
- fix directory ownership
- remove redundant buildrequires
- fix some perms

* Thu Aug 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2:0.3201-1mdk
- 0.3201

* Sat Aug 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:0.32-1mdk
- 0.32
- Be sure to test without X

* Tue May 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:0.3101-1mdk
- 0.3101
- Remove testing kludge now that Test::More was updated, adjust BuildRequires

* Sat Apr 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:0.31-1mdk
- 0.31
- make tests (in check section)

* Wed Feb 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.3009-1mdk
- 0.3009
- update summary and description
- update BuildRequires in accordance to the Makefile.PL

* Sun Aug 29 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.29-2mdk
- providing perl module to avoid the path naming issue for this module

* Tue Jul 13 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.29-1mdk
- 0.29

* Fri Jun 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2802-1mdk
- 2.802
- fix perms
- cosmetics

