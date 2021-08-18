

    def one_sided_hypo(sample_mean, pop_mean, std_dev, sample_size, alpha)
        actual_z = abs(norm.ppf(alpha))\n",
        hypo_z = (sample_mean - pop_mean) / (std_dev/sqrt(sample_size))\n",
        print('actual z value :', actual_z)\n",
        print('hypothesis z value :', hypo_z, '\\n')\n",
        if hypo_z >= actual_z:\n",
            return True\n",
        else:\n",
            return False\n",
        \n",
    alpha = 0.05\n",
    sample_mean = 108\n",
    pop_mean = 100\n",
    sample_size =  36\n",
    std_dev = 15\n",
    \n",
    print('H0 : μ <=', pop_mean)\n",
    print('H1 : μ >', pop_mean)\n",
    print('alpha value is :', alpha, '\\n')\n",
    \n",
    reject = one_sided_hypo(sample_mean, pop_mean, std_dev, sample_size, alpha)\n",
    if reject:\n",
        print('Reject NULL hypothesis')\n",
    else:\n",
        print('Failed to reject NULL hypothesis')\n",
    #variation with different parameters can be shown here"
   ]
  }
 ],