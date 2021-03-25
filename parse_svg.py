from xml.dom import minidom


def _parse_heights(heights):
    for i in range(0, len(heights)):
        heights[i] = (float(heights[i]) / 4) / 2
    return heights


def get_heights(filename):
    doc = minidom.parse(fr"output\{filename}")
    path_strings = [path.getAttribute('height') for path
                    in doc.getElementsByTagName('rect')]
    doc.unlink()
    del path_strings[0]
    print(path_strings)
    return _parse_heights(path_strings)
