Name:		python-gnutls
Version:	1.2.5
Release:	1
Group:		Sciences/Other
License:	LGPL
Summary:	Python wrapper for the GNUTLS library
Source0:	https://pypi.python.org/packages/source/p/python-gnutls/%{name}-%{version}.tar.gz
URL:		http://pypi.python.org/pypi/python-gnutls
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	python-devel

%description
This package provides a high level object oriented wrapper around libgnutls,
as well as low level bindings to the GNUTLS types and functions via ctypes.
The high level wrapper hides the details of accessing the GNUTLS library
via ctypes behind a set of classes that encapsulate GNUTLS sessions,
certificates and credentials and expose them to python applications using
a simple API.

%prep
%setup -q

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot}

%files
%py_platsitedir/gnutls
%py_platsitedir/*.egg-info


%changelog
* Mon Feb 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.4-1
+ Revision: 778140
- version update 1.2.4

* Fri Apr 08 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-3
+ Revision: 651854
- Do not call a deprecated function

* Thu Nov 04 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-2mdv2011.0
+ Revision: 593488
+ rebuild (emptylog)

* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.2.0-1mdv2010.1
+ Revision: 515899
- Update to 1.2.0
- drop patch0

* Wed Jun 03 2009 Funda Wang <fwang@mandriva.org> 1.1.8-3mdv2010.0
+ Revision: 382450
- build with gnutls 2.8

* Sat May 09 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.1.8-2mdv2010.0
+ Revision: 373581
+ rebuild (emptylog)

* Fri Mar 27 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.1.8-1mdv2009.1
+ Revision: 361539
- Import python-gnutls, version 1.1.8
  Python wrapper for the GNUTLS library
  http://pypi.python.org/pypi/python-gnutls
- python-gnutls


