# revision 17382
# category Package
# catalog-ctan /macros/latex/contrib/fncylab
# catalog-date 2010-03-09 12:54:42 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-fncylab
Version:	1.0
Release:	3
Summary:	Alter the format of \label references
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fncylab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fncylab.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fncylab.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/fncylab/fncylab.sty
%doc %{_texmfdistdir}/doc/latex/fncylab/fncylab-example.tex
%doc %{_texmfdistdir}/doc/latex/fncylab/fncylab.pdf
%doc %{_texmfdistdir}/doc/latex/fncylab/fncylab.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752002
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718472
- texlive-fncylab
- texlive-fncylab
- texlive-fncylab
- texlive-fncylab

