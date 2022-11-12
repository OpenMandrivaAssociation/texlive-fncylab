Name:		texlive-fncylab
Version:	52090
Release:	1
Summary:	Alter the format of \label references
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fncylab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fncylab.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fncylab.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX provides a mechanism for altering the appearance of
references to labels, but it's somewhat flawed, and requires
that the user manipulate internal commands. The package fixes
the flaw in LaTeX, and provides a \labelformat command for
changing the format of references to labels. The package also
provides a \Ref command to make reference to such redefined
labels at the start of a sentence.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fncylab
%doc %{_texmfdistdir}/doc/latex/fncylab

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
