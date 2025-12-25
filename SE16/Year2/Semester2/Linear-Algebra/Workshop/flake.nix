{
    description = "Jupyter Environment";

    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
        flake-utils.url = "github:numtide/flake-utils";
    };

    outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
        let
            pkgs = import nixpkgs { inherit system; };
        in {
            devShells.default = pkgs.mkShell {
            packages = with pkgs; [
                python313
                python313Packages.jupyter
                python313Packages.pip
                python313Packages.virtualenv
            ];

            # Needed for PySide6 libs
            LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";
            };
        }
    );
}

