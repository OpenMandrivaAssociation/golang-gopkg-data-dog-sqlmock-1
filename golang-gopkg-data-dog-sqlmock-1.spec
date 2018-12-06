%global goipath         gopkg.in/DATA-DOG/go-sqlmock.v1
%global forgeurl        https://github.com/DATA-DOG/go-sqlmock
Version:                1.3.0

%gometa

%global common_description %{expand:
A mock library implementing SQL driver, which has one and only purpose - to
simulate any SQL driver behavior in tests, without needing a real database
connection. It helps to maintain correct TDD workflow.

It does not require any modifications to your source code in order to test and
mock database operations. Supports concurrency and multiple database mocking.
}

Name:           %{goname}
Release:        2%{?dist}
Summary:        SQL mock driver for golang to test database interactions
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for building other packages which
use import path with %{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- First package for Fedora
