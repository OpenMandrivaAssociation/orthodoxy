Name:           orthodoxy
Version:        1.0.3
Release:        1%{?dist}
Summary:        Clang plugin to enforce custom C++ feature restrictions

License:        GPLv3+
URL:            https://github.com/d-musique/%{name}
Source0:        https://github.com/d-musique/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  clang-devel
BuildRequires:  llvm-devel
Requires:       clang

%description
Orthodoxy is a plugin for the Clang compiler, which selectively
disables specific features of the C++ language. This way, a programmer
can configure their own custom subset of the C++ language which is
tailored to a particular project.


%prep
%autosetup -p1


%build
%cmake -G Ninja -DORTHODOXY_LLVM_CONFIG=%{_bindir}/llvm-config
cd ..
%ninja -C build


%install
%ninja_install -C build


%check
ctest --test-dir build


%files
%license LICENSE.md
%doc README.md
%{_bindir}/orthodox-clang
%{_bindir}/orthodox-clang++
%{_libdir}/orthodoxy/*/orthodoxy.so
%{_libdir}/cmake/orthodoxy/orthodoxyConfig.cmake
%{_libdir}/pkgconfig/orthodoxy-for-clang*.pc
