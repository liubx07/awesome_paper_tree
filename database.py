# Copyright (c) liuboxiao. All rights reserved.

from collections import OrderedDict

tree_structure = [
    'Object Detection',
    'Base Model',
]

database = [
    {
        'Name': 'Conditional DETR for Fast Training Convergence',
        'Node': 'Object Detection',
        'Year': 2021,
        'Source': 'ICCV',
        'PDF': 'https://openaccess.thecvf.com/content/ICCV2021/papers/Meng_Conditional_DETR_for_Fast_Training_Convergence_ICCV_2021_paper.pdf',
        'Code': 'https://github.com/Atten4Vis/ConditionalDETR',
        'Tags': ['DETR',],
        'Authors': ['Depu Meng', 'Xiaokang Chen', 'Zejia Fan', 'Gang Zeng', 'Houqiang Li', 'Yuhui Yuan', 'Lei Sun', 'Jingdong Wang'],
        'Institutions': ['University of Science and Technology of China', 'Peking University', 'Microsoft Research Asia'],
        'Abstract': 'The recently-developed DETR approach applies the transformer encoder and decoder architecture to object detection and achieves promising performance. In this paper, we handle the critical issue, slow training convergence, and present a conditional cross-attention mechanism for fast DETR training. Our approach is motivated by that the cross-attention in DETR relies highly on the content embeddings for localizing the four extremities and predicting the box, which increases the need for high-quality content embeddings and thus the training difficulty. Our approach, named conditional DETR, learns a conditional spatial query from the decoder embedding for decoder multi-head cross-attention. The benefit is that through the conditional spatial query, each cross-attention head is able to attend to a band containing a distinct region, e.g., one object extremity or a region inside the object box. This narrows down the spatial range for localizing the distinct regions for object classification and box regression, thus relaxing the dependence on the content embeddings and easing the training. Empirical results show that conditional DETR converges 6.7x faster for the backbones R50 and R101 and 10x faster for stronger backbones DC5-R50 and DC5-R101. Code is available at https://github.com/Atten4Vis/ConditionalDETR.',
    },
]

def generate_readme():
    content = {}
    for node in tree_structure:
        content[node] = {}
    for paper in database:
        node = paper['Node']
        assert node in content.keys()
        year = paper['Year']
        if year not in content[node].keys():
            content[node][year] = []
        content[node][year].append(paper)
    
    readme = '# awesome_paper_tree\nOrganize awesome papers in a hierarchical tree.\n'
    for node in content.keys():
        readme += '## {}\n'.format(node)
        content_node = content[node]
        year_list = list(content_node.keys())
        year_list.sort()
        for year in year_list:
            readme += '### {}\n'.format(year)
            for paper in content_node[year]:
                readme += '- {}.\\\n{}.'.format(paper['Name'], paper['Source'])
                readme += ' [PDF]({}).'.format(paper['PDF'])
                readme += ' [Code]({}). Tags:'.format(paper['Code'])
                for tag in paper['Tags']:
                    readme += ' {},'.format(tag)
                readme = readme[:-1] + '.'
                readme += ' <details><summary>More</summary>Authors:'
                for author in paper['Authors']:
                    readme += ' {},'.format(author)
                readme = readme[:-1] + '.'
                readme += '\\\nInstitutions:'
                for institutions in paper['Institutions']:
                    readme += ' {},'.format(institutions)
                readme = readme[:-1] + '.'
                readme += '\\\nAbstract: {}</details>\n'.format(paper['Abstract'])

    with open('README.md', 'w') as f:
        f.write(readme)


if __name__ == "__main__":
    generate_readme()
