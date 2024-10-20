Name:		texlive-pmxchords
Version:	39249
Release:	2
Summary:	Produce chord information to go with pmx output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/pmxchords
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmxchords.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmxchords.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-pmxchords.bin = %{EVRD}

%description
The bundle supplements pmx, providing the means of typesetting
chords above the notes of a score. The bundle contains: macros
for typing the chords; a Lua script to transpose chord macros
to the required key signature; and support scripts for common
requirements.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/pmxchords
%{_texmfdistdir}/scripts/pmxchords/ChordsTr.lua
%{_texmfdistdir}/scripts/pmxchords/pmxchords.lua
%{_texmfdistdir}/tex/generic/pmxchords/chords.tex
%{_texmfdistdir}/tex/generic/pmxchords/chordsCZ.tex
%doc %{_mandir}/man1/pmxchords.1*
%doc %{_texmfdistdir}/doc/man/man1/pmxchords.man1.pdf
%doc %{_texmfdistdir}/doc/pmxchords/README
%doc %{_texmfdistdir}/doc/pmxchords/chordsRef.pdf
%doc %{_texmfdistdir}/doc/pmxchords/chordsRef.tex
%doc %{_texmfdistdir}/doc/pmxchords/chordsRefCZ.pdf
%doc %{_texmfdistdir}/doc/pmxchords/chordsRefCZ.tex
%doc %{_texmfdistdir}/doc/pmxchords/examples/jazz/misty/misty.pdf
%doc %{_texmfdistdir}/doc/pmxchords/examples/jazz/misty/misty.pmx
%doc %{_texmfdistdir}/doc/pmxchords/examples/jazz/schema/schema.pdf
%doc %{_texmfdistdir}/doc/pmxchords/examples/jazz/schema/schema.pmx
%doc %{_texmfdistdir}/doc/pmxchords/examples/jazz/schema/schema_full.pdf
%doc %{_texmfdistdir}/doc/pmxchords/examples/jazz/schema/schema_full.pmx
%doc %{_texmfdistdir}/doc/pmxchords/examples/noel/aj_co_to_hlasaju/aj_co_to_hlasaju.pdf
%doc %{_texmfdistdir}/doc/pmxchords/examples/noel/aj_co_to_hlasaju/aj_co_to_hlasaju.pmx
%doc %{_texmfdistdir}/doc/pmxchords/examples/noel/pasli_ovce_valasi/README
%doc %{_texmfdistdir}/doc/pmxchords/examples/noel/pasli_ovce_valasi/pasli_ovce_valasi.pdf
%doc %{_texmfdistdir}/doc/pmxchords/examples/noel/pasli_ovce_valasi/pasli_ovce_valasi.pmx
%doc %{_texmfdistdir}/doc/pmxchords/gpl-2.0.txt
%doc %{_texmfdistdir}/doc/pmxchords/pmxchords-install.pdf
%doc %{_texmfdistdir}/doc/pmxchords/pmxchords-install.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/pmxchords/pmxchords.lua pmxchords
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
