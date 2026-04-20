(function () {
    const { useMemo, useState, useEffect } = React;

    function buildInitialTowers(diskCount) {
        return [
            Array.from({ length: diskCount }, (_, index) => diskCount - index),
            [],
            []
        ];
    }

    function generateMoves(diskCount, from = 0, to = 2, aux = 1) {
        if (diskCount === 0) {
            return [];
        }

        return [
            ...generateMoves(diskCount - 1, from, aux, to),
            { from, to, disk: diskCount },
            ...generateMoves(diskCount - 1, aux, to, from)
        ];
    }

    function applyMove(towers, move) {
        const nextTowers = towers.map((tower) => [...tower]);
        const movingDisk = nextTowers[move.from].pop();

        if (movingDisk === undefined) {
            return nextTowers;
        }

        nextTowers[move.to].push(movingDisk);
        return nextTowers;
    }

    function Tower({ disks, maxDisks, label }) {
        const diskRows = [];

        for (let level = maxDisks - 1; level >= 0; level -= 1) {
            const disk = disks[level];
            const widthPercent = disk ? 28 + (disk / maxDisks) * 60 : 0;

            diskRows.push(
                React.createElement(
                    'div',
                    {
                        key: `${label}-${level}`,
                        className: 'hanoi-disk-slot d-flex justify-content-center align-items-end'
                    },
                    disk
                        ? React.createElement(
                              'div',
                              {
                                  className: 'hanoi-disk',
                                  style: { width: `${widthPercent}%` }
                              },
                              disk
                          )
                        : null
                )
            );
        }

        return React.createElement(
            'div',
            { className: 'hanoi-tower' },
            React.createElement('div', { className: 'hanoi-pole' }),
            React.createElement('div', { className: 'hanoi-disks' }, diskRows),
            React.createElement('div', { className: 'hanoi-base' }),
            React.createElement('div', { className: 'hanoi-label' }, label)
        );
    }

    function HanoiApp() {
        const [diskCount, setDiskCount] = useState(4);
        const [currentStep, setCurrentStep] = useState(0);
        const [isPlaying, setIsPlaying] = useState(false);

        const moves = useMemo(() => generateMoves(diskCount), [diskCount]);

        const towers = useMemo(() => {
            const built = buildInitialTowers(diskCount);
            for (let i = 0; i < currentStep; i += 1) {
                applyMove(built, moves[i]);
            }
            return built;
        }, [diskCount, currentStep, moves]);

        useEffect(() => {
            if (!isPlaying) {
                return undefined;
            }

            if (currentStep >= moves.length) {
                setIsPlaying(false);
                return undefined;
            }

            const timer = window.setTimeout(() => {
                setCurrentStep((prev) => Math.min(prev + 1, moves.length));
            }, 550);

            return () => window.clearTimeout(timer);
        }, [isPlaying, currentStep, moves.length]);

        function onDiskCountChange(event) {
            const value = Number(event.target.value);
            setDiskCount(value);
            setCurrentStep(0);
            setIsPlaying(false);
        }

        function resetSimulation() {
            setCurrentStep(0);
            setIsPlaying(false);
        }

        const currentMove = currentStep > 0 ? moves[currentStep - 1] : null;

        return React.createElement(
            React.Fragment,
            null,
            React.createElement(
                'div',
                { className: 'card shadow-sm border-0 mb-4' },
                React.createElement(
                    'div',
                    { className: 'card-body' },
                    React.createElement(
                        'div',
                        { className: 'row g-3 align-items-end' },
                        React.createElement(
                            'div',
                            { className: 'col-md-4' },
                            React.createElement('label', { className: 'form-label fw-semibold' }, 'Number of disks'),
                            React.createElement('input', {
                                type: 'range',
                                min: 2,
                                max: 7,
                                value: diskCount,
                                onChange: onDiskCountChange,
                                className: 'form-range'
                            }),
                            React.createElement('div', { className: 'small text-muted' }, `${diskCount} disks · ${moves.length} total moves`)
                        ),
                        React.createElement(
                            'div',
                            { className: 'col-md-8 d-flex gap-2 flex-wrap' },
                            React.createElement(
                                'button',
                                {
                                    className: 'btn btn-primary',
                                    onClick: () => setIsPlaying((prev) => !prev),
                                    disabled: currentStep >= moves.length
                                },
                                isPlaying ? 'Pause' : 'Play'
                            ),
                            React.createElement(
                                'button',
                                {
                                    className: 'btn btn-outline-primary',
                                    onClick: () => setCurrentStep((prev) => Math.min(prev + 1, moves.length)),
                                    disabled: isPlaying || currentStep >= moves.length
                                },
                                'Step'
                            ),
                            React.createElement(
                                'button',
                                {
                                    className: 'btn btn-outline-secondary',
                                    onClick: resetSimulation,
                                    disabled: currentStep === 0
                                },
                                'Reset'
                            )
                        )
                    ),
                    React.createElement(
                        'div',
                        { className: 'alert alert-light border mt-3 mb-0' },
                        currentMove
                            ? `Move ${currentStep}/${moves.length}: disk ${currentMove.disk} from ${String.fromCharCode(65 + currentMove.from)} to ${String.fromCharCode(65 + currentMove.to)}`
                            : 'Press Play or Step to start recursion visualization.'
                    )
                )
            ),
            React.createElement(
                'div',
                { className: 'hanoi-board card shadow-sm border-0 p-3 p-md-4' },
                React.createElement(
                    'div',
                    { className: 'hanoi-towers-wrap' },
                    React.createElement(Tower, { disks: towers[0], maxDisks: diskCount, label: 'A (Source)' }),
                    React.createElement(Tower, { disks: towers[1], maxDisks: diskCount, label: 'B (Aux)' }),
                    React.createElement(Tower, { disks: towers[2], maxDisks: diskCount, label: 'C (Target)' })
                )
            )
        );
    }

    const container = document.getElementById('hanoi-root');
    if (container) {
        const root = ReactDOM.createRoot(container);
        root.render(React.createElement(HanoiApp));
    }
})();
