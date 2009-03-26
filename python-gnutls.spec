Name:		python-gnutls
Version:	1.1.8
Release:	%mkrel 1
Group:		Sciences/Other
License:	LGPL
Summary:	Python wrapper for the GNUTLS library
Source:		python-gnutls-%{version}.tar.gz
URL:		http://pypi.python.org/pypi/python-gnutls
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	libgnutls-devel
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

%install
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
