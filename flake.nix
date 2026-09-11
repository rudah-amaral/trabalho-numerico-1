{
  description = "Build dependencies flake";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-25.05";
  };
  outputs = { self, nixpkgs }:
  let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in
  {
    devShells.${system}.default = pkgs.mkShell {
      buildInputs = with pkgs; [
        (python3.withPackages (p: with p; [
          virtualenv
        ]))
        texliveFull
      ];

      env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
        pkgs.stdenv.cc.cc.lib
        pkgs.libz
      ];

      shellHook = ''
        if [ ! -d "src/.venv" ]; then
          python -m venv "src/.venv"
        fi
        source src/.venv/bin/activate
        pip install -r src/requirements.txt
      '';
    };
  };
}
