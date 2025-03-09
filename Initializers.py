{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPEo1wsZvHRAtXIp9rYg59X",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/subikkshas/DA6401/blob/main/Initializers.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "5xERupAiadyO"
      },
      "outputs": [],
      "source": [
        "# Weight Initializers\n",
        "\n",
        "import numpy as np\n",
        "\n",
        "class RandomNormal:\n",
        "    \"\"\"Generates weights and biases using a normal distribution.\"\"\"\n",
        "    def __init__(self, mean=0.0, stddev=1.0):\n",
        "        self.mean = mean\n",
        "        self.stddev = stddev\n",
        "\n",
        "    def initialize(self, input_dim, output_dim):\n",
        "        \"\"\"Initializes weights and biases with a normal distribution.\"\"\"\n",
        "        weights = np.random.normal(self.mean, self.stddev, (input_dim, output_dim))\n",
        "        biases = np.random.normal(self.mean, self.stddev, (output_dim,))\n",
        "        return weights, biases\n",
        "\n",
        "\n",
        "class XavierUniform:\n",
        "    \"\"\"Implements Xavier (Glorot) uniform initialization.\"\"\"\n",
        "    def initialize(self, input_dim, output_dim):\n",
        "        \"\"\"Initializes weights and biases using the Xavier uniform method.\"\"\"\n",
        "        limit = np.sqrt(6.0 / (input_dim + output_dim))\n",
        "        weights = np.random.uniform(-limit, limit, (input_dim, output_dim))\n",
        "        biases = np.zeros(output_dim, dtype=np.float64)\n",
        "        return weights, biases\n"
      ]
    }
  ]
}