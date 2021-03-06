#!/usr/bin/env python
from manimlib import get_scene
import pprint
import sys

def main():
    with open(sys.argv[1], "r") as f:
        code = f.read()
    scene = get_scene(code, [sys.argv[2]])
    scene.render()

    pp = pprint.PrettyPrinter(indent=2)
    print("scene.initial_mobject_dict")
    pp.pprint(scene.initial_mobject_serializations)
    print()

    print("scene.scene_diffs")
    pp.pprint(scene.scene_diffs)
    print()

    print("scene.animation_diffs")
    pp.pprint(scene.animation_diffs)
    print()

    print("scene.animation_info_list")
    pp.pprint(scene.animation_info_list)
    print()

    # pp.pprint(scene.scenes_before_animation)
    # pp.pprint(scene.animation_list)
    # pp.pprint(scene.initial_mobject_dict)

if __name__ == "__main__":
    main()
